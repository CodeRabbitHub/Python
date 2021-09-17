import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", "--number1", default=0, type=int, help="first number")
    parser.add_argument("-n2", "--number2", default=0, type=int, help="second number")
    parser.add_argument(
        "-op",
        "--operation",
        help="operation",
        required=True,
        choices=["add", "subtract", "multiply"],
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="print quiet")
    parser.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    args = parser.parse_args()

    n1 = args.number1
    n2 = args.number2

    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "subtract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2

    if args.quiet:
        print(result)
    elif args.verbose:
        print(
            f"The result of {args.operation}ing {args.number1} and {args.number2} is {result}"
        )
    else:
        print("Result:", result)
