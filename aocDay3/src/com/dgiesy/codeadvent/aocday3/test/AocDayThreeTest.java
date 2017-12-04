package com.dgiesy.codeadvent.aocday3.test;

import org.junit.Test;

import com.dgiesy.codeadvent.aocday3.SpiralMemory;

public class AocDayThreeTest {
	
	@Test
	public void testFindMid() {
		for(int i = 1; i < 30; i+=2) {
			System.out.println("Find Mid for: " + i + ", found: " + SpiralMemory.stepsToMid(i));
		}
	}

}
