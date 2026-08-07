//Defining a function that returns a pair of indices of an array whose items are added to give the target value

std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target) {

//Creating a nested check the sum of items for against each index and returning a pair of items

    for (std::size_t i = 0; i < numbers.size(); i++) {
      for (std::size_t j = (i + 1); j < numbers.size(); j++) {
        if (target == (numbers[i] + numbers[j])) {
            return {i, j};
            }
         }
      }
  return {0, 0};
}     
