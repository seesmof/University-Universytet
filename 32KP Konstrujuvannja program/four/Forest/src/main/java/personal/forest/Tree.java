/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package personal.forest;

import java.util.Vector;

import personal.forest.Leaf;

/**
 *
 * @author seesm
 */
public class Tree {
  boolean isBlossomed = false;
  boolean hasBunches = false;
  boolean isCoveredWithFrost = false;
  boolean areLeavesYellow = false;
  Vector<Leaf> leaves = new Vector<>();

  void blossom() {
    this.isBlossomed = true;
    System.out.println("A tree is blossomed!");
  }

  void makeBunches() {
    this.hasBunches = true;
    System.out.println("A tree has bunches!");
  }

  void beCoveredWithFrost() {
    this.isCoveredWithFrost = true;
    System.out.println("A tree is covered with frost.");
  }

  void letLeavesBeYellow() {
    this.areLeavesYellow = true;
    for (Leaf leaf : leaves) {
      leaf.color = LeafColor.Yellow;
    }
    System.out.println("A tree has yellow leaves.");
  }
}
