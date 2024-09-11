fn main() {
    let arr = [[3, 7, 12], [40, 12, 7], [1, 3, 10]];
    let mut searched_through = 0;
    let target_value = 12;
    'outer: for i in 0..3 {
        for j in 0..3 {
            println!("{} {}", arr[i][j], i);
            searched_through += 1;
            if arr[i][j] == target_value {
                println!("found");
                break 'outer;
            }
        }
    }
    println!(
        "JESUS hedlped us search through {} elements",
        searched_through
    );
}
