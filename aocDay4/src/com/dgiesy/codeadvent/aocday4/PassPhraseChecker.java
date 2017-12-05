package com.dgiesy.codeadvent.aocday4;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class PassPhraseChecker {

	public static void main(String[] args) {
		
		int validPart1Phrases = 0;
		int badPart1Phrases = 0;
		boolean part1Good = true;
		boolean part2Good = true;
		int validPart2Phrases = 0;
		int badPart2Phrases = 0;
		String fileName = "/Users/dgiesy/ExternalGitRepo/CodeAdvent2017/aocDay4/passPhrases.txt";
		File dataFile = new File(fileName);
		try(BufferedReader br = new BufferedReader(new FileReader(dataFile))) {
		    for(String line; (line = br.readLine()) != null; ) {
		    		List<String> words = new ArrayList<String>(Arrays.asList(line.split(" ")));
		    		while(!words.isEmpty()) {
		    			String currentWord = words.get(0);
		    			words.remove(0);
		    			if(words.contains(currentWord)) {
		    				part1Good = false;
		    				part2Good = false;
//		    				System.out.println("PassPhrase failed due to dup of: " + currentWord + ", Of course this means it is also an Anagram");
		    				badPart1Phrases++;
		    				badPart2Phrases++;
		    				break;
		    			}
		    			if(containsAnagram(currentWord, words)) {
		    				badPart2Phrases++;
		    				part2Good = false;
//		    				System.out.println("PassPhrase failed part2 due to annagram of: " + currentWord);
		    				break;
		    			}
		    					    			
		    		}
		    		if(part1Good) {
					if (part2Good) {
						validPart2Phrases++;
					} else {
						part2Good = true;
					}
		    			validPart1Phrases++;
		    		}else {
		    			part1Good = true;
		    			part2Good = true;
		    		}
		    }
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		
		System.out.println("Valid Part1 Passphrases: " + validPart1Phrases);
		System.out.println("Bad Part1 Passphrases: " + badPart1Phrases);
		int part1Total = validPart1Phrases + badPart1Phrases;		
		int part2Total = validPart2Phrases + badPart2Phrases;
		System.out.println("Valid Part2 Passphrases: " + validPart2Phrases);
		System.out.println("Bad Part2 Passphrases: " + badPart2Phrases);
		System.out.println("Total Phrases scanned 1: " + part1Total);
		System.out.println("Total Phrases scanned 2: " + part2Total);
	}
	
	public static boolean containsAnagram(String word, List<String> words) {
		Iterator<String> itr = words.iterator();
		
		while (itr.hasNext()) {
			String nextWord = itr.next();
			if (isAnagram(word, nextWord)) {
				return true;
			}
		}
		return false;
	}
	
	
	/**
	 * Credit to stackoverflow user "Dany" for the isAnagram method in a response to
	 * https://stackoverflow.com/questions/4236906/finding-if-two-words-are-anagrams-of-each-other
	 * @param str1
	 * @param str2
	 * @return
	 */
	public static boolean isAnagram(String str1, String str2)
	{
	    //To get the no of occurrences of each character and store it in their ASCII location
	    int[] strCountArr1=getASCIICountArr(str1);
	    int[] strCountArr2=getASCIICountArr(str2);

	    //To Test whether the two arrays have the same count of characters. Array size 256 since ASCII 256 unique values
	    for(int i=0;i<256;i++)
	    {
	        if(strCountArr1[i]!=strCountArr2[i])
	            return false;
	    }
//	    System.out.println(str1 + " is an anagram of " + str2);
	    return true;
	}
	
	/**
	 * Credit to stackoverflow user "Dany" for the getASCIICountArr method in a response to
	 * https://stackoverflow.com/questions/4236906/finding-if-two-words-are-anagrams-of-each-other
	 * @param str
	 * @return
	 */
	public static int[] getASCIICountArr(String str)
	{
	    char c;
	    //Array size 256 for ASCII
	    int[] strCountArr=new int[256];
	    for(int i=0;i<str.length();i++)
	    {
	        c=str.charAt(i); 
	        c=Character.toUpperCase(c);// If both the cases are considered to be the same
	        strCountArr[(int)c]++; //To increment the count in the character's ASCII location
	    }
	    return strCountArr;
	}

}
