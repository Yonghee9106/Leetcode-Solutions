/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let startIndex = 0;             // start index of palindrome
    let endIndex = 0;               // end index of palindrome

    // from all elements in s, expand mirrored area to find the longest palindrome
    for (let center1 = 0; center1 < s.length; center1++) {
        // consider both odd and even palindrome
        for (let center2 of [center1, center1+1]) {
            // center1 == center2 for odd palindrome, center1+1 == center2 for even palindrome
            let l = center1;
            let r = center2;
            while(l >= 0 && r <= s.length && s[l] === s[r]) {
                [startIndex, endIndex] = (r-l+1) > (endIndex-startIndex+1) ? [l, r] : [startIndex, endIndex];
                l--, r++;
            }
        }
    }

    return s.substring(startIndex, endIndex+1);
};
