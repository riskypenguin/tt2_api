from src.utils.format_hp import format_hp

CASES = (
    (0, "0.00"),
    (42, "42.00"),
    (999, "999.00"),
    (1000, "1.00K"),
    (1001, "1.00K"),
    (1009, "1.00K"),
    (1010, "1.01K"),
    (1011, "1.01K"),
    (1100, "1.10K"),
    (1101, "1.10K"),
    (999990, "999.99K"),
    (999999, "999.99K"),
    (1000000, "1.00M"),
    (999999999, "999.99M"),
    (1000000000, "1.00B"),
    (999999999999, "999.99B"),
    (1000000000000, "1.00T"),
    (999999999999999, "999.99T"),
    (1000000000000000, "1.00Q"),
    (0.42424242, "0.00"),
    (42.42424242, "42.00"),
    (999.42424242, "999.00"),
    (1000.42424242, "1.00K"),
    (1001.42424242, "1.00K"),
    (1009.42424242, "1.00K"),
    (1010.42424242, "1.01K"),
    (1011.42424242, "1.01K"),
    (1100.42424242, "1.10K"),
    (1101.42424242, "1.10K"),
    (999990.42424242, "999.99K"),
    (999999.42424242, "999.99K"),
    (1000000.42424242, "1.00M"),
    (999999999.42424242, "999.99M"),
    (1000000000.42424242, "1.00B"),
    (999999999999.42424242, "999.99B"),
    (1000000000000.42424242, "1.00T"),
    (999999999999999.42424242, "999.99T"),
    (1000000000000000.42424242, "1.00Q"),
)


def test_format_hp():
    for case in CASES:
        i, o = case

        assert format_hp(i) == o
        assert format_hp(float(i)) == o
