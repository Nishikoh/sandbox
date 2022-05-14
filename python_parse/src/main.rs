use rustpython_parser::{ast, parser};

fn main() {
    // let python_source = "print('Hello world')";
    // let python_ast = parser::parse_expression(python_source).unwrap();
    // println!("{:#?}", python_ast);

    let python_func = "def foo(x:int) -> int:
        return x + 1";
    let python_ast = parser::parse_program(python_func).unwrap();
    println!("{:#?}", python_ast);
}
