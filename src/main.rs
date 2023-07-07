// use same_file::Handle;
use std::fs::File;
use std::io::{BufRead,BufReader,Error,ErrorKind};
use std::path::Path;

fn main() -> Result<(), Error> {
    let path_to_read = Path::new("test.txt");

    // let stdout_handle = Handle::stdout()?;
    // let handle = Handle::from_path(path_to_read)?;

    // if stdout_handle == handle {
    //     return Err(Error::new(
    //         ErrorKind::Other,
    //         "You are reading and writing from the same file"
    //     ));
    // } else {
        let file = File::open(&path_to_read)?;
        let file = BufReader::new(file);
        for (num, line) in file.lines().enumerate() {
            println!("{} : {}", num, line?.to_uppercase());
        // }
    }
    Ok(())
}