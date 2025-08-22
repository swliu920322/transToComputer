import os
import sys
import utils.Info as Util
from datetime import datetime

class RecommendationTester:
    """
    Test utility for the clothing recommendation system
    Tests different combinations of gender and country (weather) scenarios
    """
    
    def __init__(self):
        # Initialize test configuration
        self.test_results = []
        self.errors = []
        self.test_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create output directory for test results if it doesn't exist
        self.results_dir = './test_results'
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Define all possible weather types for comprehensive testing
        # Using correct weather types: clear, cloudy, rain, snow
        self.weather_types = ["clear", "cloudy", "rain", "snow"]
        
        # Validate assets directory exists
        if not os.path.exists('./assets'):
            print("WARNING: Assets directory not found!")
        
    def run_all_tests(self):
        """Run tests for all combinations of gender and country"""
        print(f"Starting recommendation tests at {self.test_timestamp}")
        print("-" * 50)
        
        # Validate dict_image configuration
        self.validate_image_config()
        
        # Test all gender and country combinations (real-world conditions)
        print("PART 1: Testing with current weather conditions")
        print("-" * 50)
        for gender_idx, gender in enumerate(Util.gender_list):
            for country_idx, country in enumerate(Util.country_list):
                self.test_recommendation(gender_idx, gender, country_idx, country)
        
        # Test all gender and weather type combinations (comprehensive coverage)
        print("\nPART 2: Testing all possible weather types")
        print("-" * 50)
        for gender_idx, gender in enumerate(Util.gender_list):
            for weather_type in self.weather_types:
                self.test_weather_type(gender_idx, gender, weather_type)
        
        self.generate_report()
    
    def validate_image_config(self):
        """Validate dict_image configuration to ensure all combinations are defined"""
        print("Validating image configuration...")
        valid = True
        
        # Check if dict_image exists and has correct structure
        if not hasattr(Util, 'dict_image'):
            print("ERROR: Util.dict_image not found!")
            self.errors.append("Util.dict_image configuration missing")
            return False
        
        # Print the structure of dict_image for debugging
        print("dict_image structure:")
        for gender in Util.gender_list:
            if gender not in Util.dict_image:
                print(f"  ERROR: Missing gender '{gender}' in dict_image")
                valid = False
                self.errors.append(f"Missing gender '{gender}' in dict_image")
                continue
                
            print(f"  {gender}:")
            for weather_type in self.weather_types:
                if weather_type not in Util.dict_image[gender]:
                    print(f"    ERROR: Missing weather type '{weather_type}' for gender '{gender}'")
                    valid = False
                    self.errors.append(f"Missing weather type '{weather_type}' for gender '{gender}'")
                    continue
                    
                image_path = Util.dict_image[gender][weather_type]
                full_path = f'./assets/{image_path}'
                exists = os.path.exists(full_path)
                print(f"    {weather_type}: {image_path} - {'EXISTS' if exists else 'MISSING'}")
                
                if not exists:
                    self.errors.append(f"Missing asset file: {full_path}")
                    valid = False
        
        print(f"Configuration validation {'PASSED' if valid else 'FAILED'}")
        print("-" * 30)
        return valid
    
    def test_recommendation(self, gender_idx, gender, country_idx, country):
        """Test a specific gender and country combination"""
        try:
            print(f"Testing: Gender={gender}, Country={country}")
            
            # Get weather information for the country
            weather = Util.get_weather_by_country(country)
            weather_type = Util.get_weather_by_response(weather)
            
            # Check if weather_type is valid
            if weather_type not in self.weather_types:
                error_msg = f"Invalid weather type '{weather_type}' returned for {country}"
                print(f"  ERROR: {error_msg}")
                self.errors.append(error_msg)
                return
            
            # Check if the weather_type exists in dict_image for this gender
            if gender not in Util.dict_image or weather_type not in Util.dict_image[gender]:
                error_msg = f"Missing configuration for gender='{gender}', weather_type='{weather_type}'"
                print(f"  ERROR: {error_msg}")
                self.errors.append(error_msg)
                return
            
            # Get recommended clothing image
            image_path = f'./assets/{Util.dict_image[gender][weather_type]}'
            
            # Check if the image exists
            image_exists = os.path.exists(image_path)
            
            # Record test results
            result = {
                'test_type': 'country_based',
                'gender': gender,
                'country': country,
                'weather': weather,
                'weather_type': weather_type,
                'image_path': image_path,
                'image_exists': image_exists,
                'success': image_exists
            }
            
            self.test_results.append(result)
            
            # Print test result
            status = "PASS" if image_exists else "FAIL"
            print(f"  Weather: {weather}, Type: {weather_type}")
            print(f"  Image: {image_path}")
            print(f"  Result: {status}")
            print("-" * 30)
            
        except Exception as e:
            error_msg = f"Error testing {gender} in {country}: {str(e)}"
            print(f"  ERROR: {error_msg}")
            print("-" * 30)
            self.errors.append(error_msg)
    
    def test_weather_type(self, gender_idx, gender, weather_type):
        """Test a specific gender and weather type combination"""
        try:
            print(f"Testing: Gender={gender}, Weather Type={weather_type}")
            
            # Check if the weather_type exists in dict_image for this gender
            if gender not in Util.dict_image or weather_type not in Util.dict_image[gender]:
                error_msg = f"Missing configuration for gender='{gender}', weather_type='{weather_type}'"
                print(f"  ERROR: {error_msg}")
                self.errors.append(error_msg)
                
                # Record test results as failure
                result = {
                    'test_type': 'weather_type_based',
                    'gender': gender,
                    'country': 'N/A',
                    'weather': 'N/A',
                    'weather_type': weather_type,
                    'image_path': 'CONFIGURATION_MISSING',
                    'image_exists': False,
                    'success': False
                }
                
                self.test_results.append(result)
                print(f"  Result: FAIL (Missing configuration)")
                print("-" * 30)
                return
            
            # Get recommended clothing image directly for this weather type
            image_path = f'./assets/{Util.dict_image[gender][weather_type]}'
            
            # Check if the image exists
            image_exists = os.path.exists(image_path)
            
            # Record test results
            result = {
                'test_type': 'weather_type_based',
                'gender': gender,
                'country': 'N/A',
                'weather': 'N/A',
                'weather_type': weather_type,
                'image_path': image_path,
                'image_exists': image_exists,
                'success': image_exists
            }
            
            self.test_results.append(result)
            
            # Print test result
            status = "PASS" if image_exists else "FAIL"
            print(f"  Weather Type: {weather_type}")
            print(f"  Image: {image_path}")
            print(f"  Result: {status}")
            print("-" * 30)
            
        except Exception as e:
            error_msg = f"Error testing {gender} with weather type {weather_type}: {str(e)}"
            print(f"  ERROR: {error_msg}")
            print("-" * 30)
            self.errors.append(error_msg)
    
    def generate_report(self):
        """Generate a summary report of test results"""
        # Calculate test statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        # Calculate statistics for each test type
        country_tests = [r for r in self.test_results if r['test_type'] == 'country_based']
        weather_type_tests = [r for r in self.test_results if r['test_type'] == 'weather_type_based']
        
        country_passed = sum(1 for r in country_tests if r['success'])
        weather_type_passed = sum(1 for r in weather_type_tests if r['success'])
        
        # Print summary to console
        print("\n" + "=" * 50)
        print("TEST SUMMARY")
        print("=" * 50)
        print(f"Total tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success rate: {passed_tests/total_tests*100:.2f}%")
        
        print("\nCountry-based tests:")
        print(f"  Total: {len(country_tests)}")
        print(f"  Passed: {country_passed}")
        if len(country_tests) > 0:
            print(f"  Success rate: {country_passed/len(country_tests)*100:.2f}%")
        
        print("\nWeather type tests:")
        print(f"  Total: {len(weather_type_tests)} (expected: {len(Util.gender_list) * len(self.weather_types)})")
        print(f"  Passed: {weather_type_passed}")
        if len(weather_type_tests) > 0:
            print(f"  Success rate: {weather_type_passed/len(weather_type_tests)*100:.2f}%")
        
        if self.errors:
            print("\nErrors encountered:")
            for error in self.errors:
                print(f"- {error}")
        
        # Write detailed results to file
        report_file = os.path.join(self.results_dir, f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(report_file, 'w') as f:
            f.write(f"Clothes Recommendation Test Report\n")
            f.write(f"Generated: {self.test_timestamp}\n")
            f.write("=" * 50 + "\n\n")
            
            # Write weather type test results first (comprehensive coverage)
            f.write("COMPREHENSIVE WEATHER TYPE TESTS:\n")
            f.write("-" * 40 + "\n\n")
            
            weather_type_results = {}
            for gender in Util.gender_list:
                weather_type_results[gender] = {}
                for weather_type in self.weather_types:
                    weather_type_results[gender][weather_type] = "Not Tested"
            
            for result in weather_type_tests:
                gender = result['gender']
                weather_type = result['weather_type']
                weather_type_results[gender][weather_type] = "PASS" if result['success'] else "FAIL"
            
            # Create a table for weather type tests
            f.write("Gender/Weather | Clear  | Cloudy | Rain   | Snow   \n")
            f.write("--------------+--------+--------+--------+--------\n")
            
            for gender in Util.gender_list:
                row = f"{gender:<14}| "
                for weather_type in self.weather_types:
                    status = weather_type_results[gender][weather_type]
                    row += f"{status:<7} | "
                f.write(row + "\n")
            
            f.write("\n\n")
            
            # Write missing files section if needed
            missing_files = [r for r in self.test_results if not r['image_exists'] and r['image_path'] != 'CONFIGURATION_MISSING']
            if missing_files:
                f.write("MISSING IMAGE FILES:\n")
                f.write("-" * 40 + "\n\n")
                for result in missing_files:
                    f.write(f"- {result['image_path']}\n")
                f.write("\n\n")
            
            # Write detailed test results
            f.write("DETAILED TEST RESULTS:\n")
            f.write("-" * 40 + "\n\n")
            
            for i, result in enumerate(self.test_results, 1):
                f.write(f"Test #{i}:\n")
                f.write(f"  Test Type: {result['test_type']}\n")
                f.write(f"  Gender: {result['gender']}\n")
                if result['test_type'] == 'country_based':
                    f.write(f"  Country: {result['country']}\n")
                    f.write(f"  Weather: {result['weather']}\n")
                f.write(f"  Weather Type: {result['weather_type']}\n")
                f.write(f"  Image Path: {result['image_path']}\n")
                f.write(f"  Image Exists: {result['image_exists']}\n")
                f.write(f"  Result: {'PASS' if result['success'] else 'FAIL'}\n")
                f.write("\n")
            
            # Write summary statistics
            f.write("SUMMARY:\n")
            f.write("-" * 40 + "\n\n")
            f.write(f"Total tests: {total_tests}\n")
            f.write(f"Passed: {passed_tests}\n")
            f.write(f"Failed: {failed_tests}\n")
            f.write(f"Success rate: {passed_tests/total_tests*100:.2f}%\n\n")
            
            f.write("Country-based tests:\n")
            f.write(f"  Total: {len(country_tests)}\n")
            f.write(f"  Passed: {country_passed}\n")
            if len(country_tests) > 0:
                f.write(f"  Success rate: {country_passed/len(country_tests)*100:.2f}%\n\n")
            
            f.write("Weather type tests:\n")
            f.write(f"  Total: {len(weather_type_tests)} (expected: {len(Util.gender_list) * len(self.weather_types)})\n")
            f.write(f"  Passed: {weather_type_passed}\n")
            if len(weather_type_tests) > 0:
                f.write(f"  Success rate: {weather_type_passed/len(weather_type_tests)*100:.2f}%\n\n")
            
            if self.errors:
                f.write("ERRORS ENCOUNTERED:\n")
                f.write("-" * 40 + "\n\n")
                for error in self.errors:
                    f.write(f"- {error}\n")
        
        print(f"\nDetailed report saved to: {report_file}")


if __name__ == "__main__":
    # Create and run the tester
    tester = RecommendationTester()
    tester.run_all_tests() 