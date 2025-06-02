/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package personal.individual;

/**
 *
 * @author seesm
 */
public class Range {
    int start;
    int finish;

    public Range(int start, int finish) {
        this.start = start;
        this.finish = finish;
    }

    public boolean strictContains(int k) {
        return k >= start && k <= finish;
    }

    public boolean looseContains(int k) {
        return k > start && k <= finish;
    }
}
