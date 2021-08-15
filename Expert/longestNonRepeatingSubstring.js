const longestNonRepeatingSubstring = (str) => {
  let longestSubString = '';
  let current = '';
  for(const char of str) {
    if (current.includes(char)) {
      current = current.slice(current.indexOf(char) + 1);
    }
    current = `${current}${char}`;
    longestSubString = longestSubString.length < current.length ? current : longestSubString;
  }
  return longestSubString;
};

console.log(longestNonRepeatingSubstring('kjlmjsdfewii'));
