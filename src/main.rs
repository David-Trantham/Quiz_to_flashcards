
use std::env::consts;
use std::fs::File;
use std::io::{Write, BufRead,BufReader, BufWriter, Error};
use std::path::Path;

fn initialize_output() -> Result<(), Error> {
    
}
fn main() -> Result<(), Error> {
    let input_path = Path::new("test.txt");
    let output_path = Path::new("output.txt");
    let mut buffer = Vec::new;
    let buffer = BufWriter::new(buffer);

    // let file = File::open(&input_path)?;
    // let file = BufReader::new(file);
    // for (num, line) in file.lines().enumerate() {
    //     println!("{} : {}", num, line?.to_uppercase());
    let mut output = File::create(output_path)?;
    write!(output, "initialize")?;

    let input = File::open(input_path)?;
    let input = BufReader::new(input);
    const CORRECT_ANSWER_ID: &str = "( Missed)";
    const END_OF_QUESTION: &str = "Your answer to this question is incorrect";
    for (num, line) in input.lines().enumerate(){
        let this_line = line?;
        //If we are still "Within a single question"
        if !this_line.starts_with(END_OF_QUESTION) {
            write!(buffer, "hi there");
        }

    }
    Ok(())
}