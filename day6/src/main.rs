use std::fs::File;
use std::io::{self, Read};

fn ways(time: i64, distance: i64) -> i64 {
    let mut ways = 0;
    for speed in 0..time {
        if speed * (time - speed) > distance {
            ways += 1;
        }
    }
    ways
}
fn concat_int(a: i64, b: i64) -> i64 {
    let m_str = format!("{}{}", a,b);
    m_str.parse::<i64>().unwrap()
}

fn main() -> io::Result<()> {
    let mut f = File::open("input")?;
    let mut buffer = String::new();
    f.read_to_string(&mut buffer)?;
    let mut lines = buffer.lines();
    let mut time_line = lines.next().unwrap().split_whitespace();
    let mut distance_line = lines.next().unwrap().split_whitespace();
    let mut time_p2: i64 = 0;
    let mut distance_p2: i64 = 0 ;
    let mut p1 = 1;
    time_line.next();
    distance_line.next();
    
    while let Some(time) = time_line.next() {
        let distance = distance_line.next().unwrap().parse::<i64>().unwrap();
        let time = time.parse::<i64>().unwrap();
        if time_p2 == 0 {
            time_p2 = time;
            distance_p2 = distance;
        } else {
            time_p2 = concat_int(time_p2, time);
            distance_p2 = concat_int(distance_p2, distance);
        }
        p1 *=  ways(time, distance);
    }
    println!("Part 1: {}", p1);
    println!("Part 2: {}", ways(time_p2, distance_p2));

    Ok(())
    
}
