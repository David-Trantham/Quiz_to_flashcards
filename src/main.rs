use std::fs::File;
use std::io::{self, Read};
fn main() {
    let file= File::open("test.txt")?;
    println!("{}", file);
}
