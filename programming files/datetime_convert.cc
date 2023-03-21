// Include libraries
#include <iostream>
#include <iomanip>
#include <sstream>
#include <chrono>


int main()
{
    // Initialize sample string
    std::string date_str = "2022-03-17 10:45:30";
    
    // Initialize date_obj
    std::tm date_obj = {};
    
    // Feed sample string to a string stream
    std::istringstream ss(date_str);
    
    // Parse in time from string string
    ss >> std::get_time(&date_obj, "%Y-%m-%d %H:%M:%S");
    
    std::stringstream formatted_date_ss;
    formatted_date_ss << std::put_time(&date_obj, "%m/%d/%Y %H:%M:%S");
    std::string formatted_date = formatted_date_ss.str();

    std::cout << formatted_date << std::endl;

    return 0;
}
