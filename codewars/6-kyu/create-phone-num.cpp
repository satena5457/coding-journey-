#include <string>
//A program for creating phone number from the given array of numbers
std::string createPhoneNumber(const int arr[10]){
 //declaration of the string res
  std::string res;
  //concatenating the array into the string res
  for (int i = 0; i < 10; i++) {
    res += std::to_string(arr[i]);
    }
  //inserting characters like (, ) , - at the specific position in the string 
  res.insert(0, "(");
  res.insert(4, ") ");
  res.insert(9, "-");
  
  return res;
}
