/*
 * @author Darrin Giesy
 * 
 */
package com.dgiesy.codeadvent.aocday3;

/**
 * The Class SpiralMemory.
 */
public class SpiralMemory {

	/**
	 * The main method.
	 *
	 * @param args the arguments
	 */
	public static void main(String[] args) {
		
		int testData[] = {1, 12, 23, 212, 530, 700, 1024, 289326};
		for(int i =0; i < testData.length; i++) {
			System.out.println("Hopefully... " + findDistanceToCenter(testData[i]));
		}		
	}
	
	public static int findNextValue(int value) {
		int nextVal = value;
		
		return nextVal;
	}
	
	public static int findDistanceToCenter(int address) {
		
		int nextSqrt = (int) Math.ceil(Math.sqrt(address));
		int sideLength;
		if (nextSqrt % 2 == 0) {
			sideLength = nextSqrt +1;
		}else {
			sideLength = nextSqrt;
		}
		int stepsFromCornerToMid = stepsToMid(sideLength);
		int fromMid;
		
		int lrCorner = (int) Math.pow((sideLength), (2));
		int llCorner = lrCorner - (sideLength - 1);
		int ulCorner = llCorner - (sideLength - 1);
		int urCorner = ulCorner - (sideLength - 1);
		
		int southCenter = (int) Math.pow(sideLength, 2) - stepsFromCornerToMid;
		int westCenter = southCenter - (sideLength - 1);
		int northCenter = westCenter - (sideLength - 1);
		int eastCenter = northCenter - (sideLength - 1);
		
		if (address > llCorner) {
			fromMid = (int)Math.abs(address - southCenter);
		}else if(address > ulCorner) {
			fromMid = (int)Math.abs(address - westCenter);
		}else if(address > urCorner) {
			fromMid = (int)Math.abs(address - northCenter);
		}else{
			fromMid = (int)Math.abs(address - eastCenter);
		}
//		System.out.println("distance from mid: " + fromMid);
		int fixedDistance = stepsFromCornerToMid;
//		System.out.println("fixedD: " + fixedDistance);
		int fullDistance = fromMid + fixedDistance;
		return fullDistance;		
	}
	
	public static int stepsToMid(int sideLength) {
		return (sideLength - 1)/2;
	}
	
	
	
	

}
