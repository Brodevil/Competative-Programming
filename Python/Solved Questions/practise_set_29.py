# Python practise - Compitative Programming (From Adventofcode 2020) = Day 1 Report Repair

""" 
Day 1

--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.


For example, suppose your expense report contained the following:
1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

To begin, get your puzzle input. (https://adventofcode.com/2020/day/1/input)

"""

data = """
1632
1438
1811
1943
1883
1698
1976
1972
1794
1726
1850
1789
1524
1701
1454
1594
1655
1018
1828
1867
1959
1541
1596
1998
1916
1894
1727
1812
1800
1897
1534
1712
1825
1629
1827
81
1855
1621
1694
1663
1793
1685
1616
1899
1688
1652
1719
1589
1649
1742
1905
922
1695
1747
1989
1968
1678
1709
1938
1920
1429
1556
2005
1728
1484
1746
1702
1456
1917
1670
1433
1538
1806
1667
1505
963
1478
2003
1955
1689
1490
1523
1615
1784
1624
583
1465
1443
1489
1873
1485
1773
1704
352
505
1705
1844
1599
1778
1846
1533
1535
1965
1987
828
1755
1823
1639
1981
1763
1758
1819
1569
1580
358
1786
1964
1604
1805
1822
1941
1993
1939
1975
1966
1852
1310
1687
1718
641
1715
1995
1603
1444
1641
1961
1536
1771
1267
1749
1944
1519
1445
1818
1558
1922
1452
1901
1915
1957
1840
1785
1946
1683
1918
1847
1690
1716
1627
1571
1985
1455
435
1856
1527
1660
1555
1557
1591
1906
1646
1656
1620
1618
1598
1606
1808
1509
1551
1723
1835
1610
1820
1942
1767
1549
1607
1781
1612
1864
2007
1908
1650
1449
1886
1878
1895
1869
1469
1507
"""
# Author = Abhinav
# Date = 3 May 2021
# Pourpose = Just for the python practise to not just learn python also to expert it


def calculation(lst):
    for element in lst:
        for value in lst:
            if element + value == 2020:  # this is part one answer
                print(element * value)

            for vlaue2 in lst:
                if element + value + vlaue2 == 2020:
                    print(element * value * vlaue2)  # this will part 2 answer


if __name__ == "__main__":
    data = list(map(int, data.split()))
    calculation(data)
