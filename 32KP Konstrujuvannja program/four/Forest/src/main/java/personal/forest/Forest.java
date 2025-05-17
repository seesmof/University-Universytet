/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package personal.forest;

import personal.forest.Leaf;
import personal.forest.LeafColor;

/**
 *
 * @author seesm
 */
public class Forest {
    public static void main(String[] args) {
        Tree tree = new Tree();

        Leaf one = new Leaf();
        one.color = LeafColor.Green;
        Leaf two = new Leaf();
        two.color = LeafColor.Orange;
        Leaf three = new Leaf();
        three.color = LeafColor.Green;

        tree.leaves.add(one);
        tree.leaves.add(two);
        tree.leaves.add(three);

        tree.letLeavesBeYellow();
        System.out.println(tree.leaves.elementAt(1).color);
    }
}
