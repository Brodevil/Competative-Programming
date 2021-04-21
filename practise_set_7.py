# Python Practise Set 7 (Medium, 10 points) -  Search Engine
"""
Search Engine:

You are given few sentences as a list (Python list of sentences).Take a query string as a input from the user.
You have to pull out the sentences matching a query inputted by the user in decreasing order of relevance after convertin every word in the query and the sentence to lowercase.
Most relevent sentence is the one with the maximum number of matching words with query.

Secntence = ["This is practise ", "this string will be too big that we will not able to even find anything sir", "Python is too best programming laguages", "Python Porgramming with PyCharm and VS code", "Best python pratise is to just practise and learn many things"]


Input:

Please input your query string :
"python"


Output:

About 3 result (00.89 sec.):

1. Best python pratise is to just practise and learn many things
2. Python Porgramming with PyCharm and VS
3. Python is too best programming laguages


"""

sentences = [
    """Python Insider
    Python core development news and information.

    Tuesday, April 6, 2021
    Python 3.10.0a7 is now available for testing
    Brrrrr… do you feel that? That’s the chill of beta freeze coming closer. Meanwhile, your friendly CPython release team doesn’t rest even on holidays and we have prepared a shiny new release for you: Python 3.10.0a7.

    Get the new release here:

    https://www.python.org/downloads/release/python-3100a7/

    Python 3.10.0a7

    Release Date: April 5, 2021

    This is an early developer preview of Python 3.10

    Major new features of the 3.10 series, compared to 3.9
    Python 3.10 is still in development. This release, 3.10.0a7 is the last of seven planned alpha releases. Alpha releases are intended to make it easier to test the current state of new features and bug fixes and to test the release process. During the alpha phase, features may be added up until the start of the beta phase (2021-05-03) and, if necessary, may be modified or deleted up until the release candidate phase (2021-10-04). Please keep in mind that this is a preview release and its use is not recommended for production environments.

    Many new features for Python 3.10 are still being planned and written. Among the new major new features and changes so far:

    PEP 623 – Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
    PEP 604 – Allow writing union types as X | Y
    PEP 612 – Parameter Specification Variables
    PEP 626 – Precise line numbers for debugging and other tools.
    bpo-38605: from __future__ import annotations (PEP 563) is now the default.
    PEP 618 – Add Optional Length-Checking To zip.
    bpo-12782: Parenthesized context managers are now officially allowed.
    PEP 632 – Deprecate distutils module.
    PEP 613 – Explicit Type Aliases
    PEP 634 – Structural Pattern Matching: Specification
    PEP 635 – Structural Pattern Matching: Motivation and Rationale
    PEP 636 – Structural Pattern Matching: Tutorial
    PEP 644 – Require OpenSSL 1.1.1 or newer
    PEP 624 – Remove Py_UNICODE encoder APIs
    PEP 597 – Add optional EncodingWarning
    (Hey, fellow core developer, if a feature you find important is missing from this list, let Pablo know.)
    The next pre-release of Python 3.10 will be 3.10.0b1 ( the first beta release and feature freeze ), currently scheduled for Monday, 2021-05-03.

    More resources
    Online Documentation
    PEP 619, 3.10 Release Schedule
    Report bugs at https://bugs.python.org.
    Help fund Python and its community.
    And now for something completely different
    In physics, the twin paradox is a thought experiment in special relativity involving identical twins, one of whom makes a journey into space in a high-speed rocket and returns home to find that the twin who remained on Earth has aged more. This result appears puzzling because each twin sees the other twin as moving, and so, as a consequence of an incorrect and naive application of time dilation and the principle of relativity, each should paradoxically find the other to have aged less. However, this scenario can be resolved by realising that the travelling twin is undergoing acceleration, which makes him a non-inertial observer. In both views, there is no symmetry between the spacetime paths of the twins. Therefore, the twin paradox is not a paradox in the sense of a logical contradiction.

    We hope you enjoy those new releases!

    Thanks to all of the many volunteers who help make Python Development and these releases possible! Please consider supporting our efforts by volunteering yourself or through organization contributions to the Python Software Foundation.
    Your friendly release team,
    Pablo Galindo Salgado @pablogsal
    Ned Deily @nad
    Steve Dower @steve.dower""",

    """
    Python Insider
    Python core development news and information.

    Sunday, April 4, 2021
    Python 3.9.4 hotfix is now available
    Python 3.9.3 was released two days ago on Friday, April 2nd. It contains important security content listed below for reference. Unfortunately, it also introduced an unintentional ABI incompatibility, making some C extensions built with Python 3.9.0 - 3.9.2 crash with Python 3.9.3 on 32-bit systems. To minimize disruption, I decided to recall 3.9.3 and introduce this hotfix release: 3.9.4.

    We highly recommend upgrading your Python 3.9 installations to 3.9.4 at your earliest convenience.

    Get it here:

    https://www.python.org/downloads/release/python-394/

    What is “ABI compatibility”?
    Python guarantees that within a given language series (like the current 3.9) binary extensions written in C or C++ and compiled against headers of one release (like 3.9.0) will be importable from other versions in the same series (like 3.9.3). If this weren’t the case, library authors would have to ship separate binary wheels on PyPI for every single bugfix release of Python. That would be very inconvenient.

    What broke in Python 3.9.3?
    In a fix for a corner-case crash around recursion limits and exceptions, the PyThreadState struct needed to change. While PyThreadState’s only documented public member is the *interp field, it’s not uncommon for C extensions to access other fields in this struct as well.

    When I approved the backport of this fix, I missed the fact that the variable size change would change the memory layout of said struct on 32-bit systems (on 64-bit systems alignment rules made the size change backwards compatible). Merging the backport was a mistake, and so 3.9.4 reverts it to restore compatibility with binary extensions built against Python 3.9.0 - 3.9.2. Details in bpo-43710.

    Security Content in Python 3.9.3
    bpo-43631: high-severity CVE-2021-3449 and CVE-2021-3450 were published for OpenSSL, it’s been upgraded to 1.1.1k in CI, and macOS and Windows installers.
    bpo-42988: CVE-2021-3426: Remove the getfile feature of the pydoc module which could be abused to read arbitrary files on the disk (directory traversal vulnerability). Moreover, even source code of Python modules can contain sensitive data like passwords. Vulnerability reported by David Schwörer.
    bpo-43285: ftplib no longer trusts the IP address value returned from the server in response to the PASV command by default. This prevents a malicious FTP server from using the response to probe IPv4 address and port combinations on the client network. Code that requires the former vulnerable behavior may set a trust_server_pasv_ipv4_address attribute on their ftplib.FTP instances to True to re-enable it.
    bpo-43439: Add audit hooks for gc.get_objects(), gc.get_referrers() and gc.get_referents(). Patch by Pablo Galindo.
    Release Calendar
    Maintenance releases for the 3.9 series will continue at regular bi-monthly intervals, with 3.9.5 planned for May 3rd 2021 as well.

    What’s new?
    The Python 3.9 series contains many new features and optimizations over 3.8. See the “What’s New in Python 3.9 ” document for more information about features included in the 3.9 series. We also have a detailed change log for 3.9.3 specifically.

    Detailed information about all changes made in version 3.8.9 can be found in its respective changelog.

    We hope you enjoy those new releases!
    Thanks to all of the many volunteers who help make Python Development and these releases possible! Please consider supporting our efforts by volunteering yourself or through organization contributions to the Python Software Foundation.

    Your friendly release team,
    Łukasz Langa @ambv
    Ned Deily @nad
    Steve Dower @steve.dower
    

    Posted by Łukasz Langa at 3:19 PM """,

    """
    Optimize Windows for better performance
    Windows 7
    Here are some tips to help you optimize Windows 7 for faster performance.

    Try the Performance troubleshooter
    The first thing that you can try is the Performance troubleshooter, which can automatically find and fix problems. The Performance troubleshooter checks issues that might slow down your computer's performance, such as how many users are currently logged on to the computer and whether multiple programs are running at the same time.

    Open the Performance troubleshooter by clicking the Start Start button icon button, and then clicking Control Panel. In the search box, type troubleshooter, and then click Troubleshooting. Under System and Security, click Check for performance issues.

    Delete programs you never use
    Many PC manufacturers pack new computers with programs you didn't order and might not want. These often include trial editions and limited-edition versions of programs that software companies hope you'll try, find useful, and then pay to upgrade to full versions or newer versions. If you decide you don't want them, keeping the software on your computer might slow it down by using precious memory, disk space, and processing power.

    It's a good idea to uninstall all the programs you don't plan to use. This should include both manufacturer-installed software and software you installed yourself but don't want any more—especially utility programs designed to help manage and tune your computer's hardware and software. Utility programs such as virus scanners, disk cleaners, and backup tools often run automatically at startup, quietly chugging along in the background where you can't see them. Many people have no idea they're even running.

    Even if your PC is older, it might contain manufacturer-installed programs that you never noticed or have since forgotten about. It's never too late to remove these and get rid of the clutter and wasted system resources. Maybe you thought you might use the software someday, but never did. Uninstall it and see if your PC runs faster.

    Limit how many programs run at startup
    Many programs are designed to start automatically when Windows starts. Software manufacturers often set their programs to open in the background, where you can't see them running, so they'll open right away when you click their icons. That's helpful for programs you use a lot, but for programs you rarely or never use, this wastes precious memory and slows down the time it takes Windows to finish starting up.

    Decide for yourself if you want a program to run at startup.

    But how can you tell what programs run automatically at startup? Sometimes this is obvious, because the program adds an icon to the notification area on the taskbar, where you can see it running. Look there to see if there are any programs running that you don’t want to start automatically. Point to each icon to see the program name. Be sure to click the Show hidden icons button so you don't miss any icons.

    Even after you check the notification area, you might still miss some programs that run automatically at startup. AutoRuns for Windows, a free tool that you can download from the Microsoft website, shows you all of the programs and processes that run when you start Windows. You can stop a program from running automatically when Windows starts by opening the AutoRuns for Windows program, and then by clearing the check box next to the name of the program you want to stop. AutoRuns for Windows is designed for advanced users.

    Defragment your hard disk
    Fragmentation makes your hard disk do extra work that can slow down your computer. Disk Defragmenter rearranges fragmented data so your hard disk can work more efficiently. Disk Defragmenter runs on a schedule, but you can also defragment your hard disk manually.

    Clean up your hard disk
    Unnecessary files on your hard disk take up disk space and can slow down your computer. Disk Cleanup removes temporary files, empties the Recycle Bin, and removes a variety of system files and other items that you no longer need.

    Run fewer programs at the same time
    Sometimes changing your computing behavior can have a big impact on your PC's performance. If you're the type of computer user who likes to keep eight programs and a dozen browser windows open at once—all while sending instant messages to your friends—don't be surprised if your PC bogs down. Keeping a lot of e‑mail messages open can also use up memory.

    If you find your PC slowing down, ask yourself if you really need to keep all your programs and windows open at once. Find a better way to remind yourself to reply to e‑mail messages rather than keeping all of them open.

    Make sure you're only running one antivirus program. Running more than one antivirus program can also slow down your computer. Fortunately, if you're running more than one antivirus program, Action Center notifies you and can help you fix the problem.

    Turn off visual effects
    If Windows is running slowly, you can speed it up by disabling some of its visual effects. It comes down to appearance versus performance. Would you rather have Windows run faster or look prettier? If your PC is fast enough, you don't have to make this tradeoff, but if your computer is just barely powerful enough for Windows 7, it can be useful to scale back on the visual bells and whistles.

    You can choose which visual effects to turn off, one by one, or you can let Windows choose for you. There are 20 visual effects you can control, such as the transparent glass look, the way menus open or close, and whether shadows are displayed.

    To adjust all visual effects for best performance:

    Open Performance Information and Tools by clicking the Start  Start button icon button, and then clicking Control Panel. In the search box, type Performance Information and Tools, and then, in the list of results, click Performance Information and Tools.

    Click Adjust visual effectsAdministrator permission required. If you're prompted for an administrator password or confirmation, type the password or provide confirmation.

    Click the Visual Effects tab, click Adjust for best performance, and then click OK. (For a less drastic option, select Let Windows choose what’s best for my computer.)

    Restart regularly
    This tip is simple. Restart your PC at least once a week, especially if you use it a lot. Restarting a PC is a good way to clear out its memory and ensure that any errant processes and services that started running get shut down.

    Restarting closes all the software running on your PC—not only the programs you see running on the taskbar, but also dozens of services that might have been started by various programs and never stopped. Restarting can fix mysterious performance problems when the exact cause is hard to pinpoint.

    If you keep so many programs, e‑mail messages, and websites open that you think restarting is a hassle, that's probably a sign you should restart your PC. The more things you have open and the longer you keep them running, the greater the chances your PC will bog down and eventually run low on memory.

    Add more memory
    This isn't a guide to buying hardware that will speed up your computer. But no discussion of how to make Windows run faster would be complete without mentioning that you should consider adding more random access memory (RAM) to your PC.

    If a computer running Windows 7 seems too slow, it's usually because the PC doesn't have enough RAM. The best way to speed it up is to add more.

    Windows 7 can run on a PC with 1 gigabyte (GB) of RAM, but it runs better with 2 GB. For optimal performance, boost that to 3 GB or more.

    Another option is to boost the amount of memory by using Windows‌ ReadyBoost. This feature allows you to use the storage space on some removable media devices, such as USB flash drives, to speed up your computer. It’s easier to plug a flash drive into a USB port than to open your PC case and plug memory modules into its motherboard.

    Check for viruses and spyware
    If your PC is running slowly, it's possible that it's infected with a virus or spyware. This is not as common as the other problems, but it's something to consider. Before you worry too much, check your PC using antispyware and antivirus programs.

    A common symptom of a virus is a much slower-than-normal computer performance. Other signs include unexpected messages that pop up on your PC, programs that start automatically, or the sound of your hard disk constantly working.

    Spyware is a type of program that's installed, usually without your knowledge, to watch your activity on the Internet. You can check for spyware with Windows Defender or other antispyware programs.

    The best way to deal with viruses is to prevent them in the first place. Always run antivirus software and keep it up to date. Even if you take such precautions, however, it's possible for your PC to become infected.

    Check your computer's speed
    If you try these tips and your computer is still too slow, you might need a new PC or some hardware upgrades, such as a new hard disk or faster video card. There's no need to guess the speed of your computer, however. Windows provides a way to check and rate your PC's speed with a tool called the Windows Experience Index.

    The Windows Experience Index rates your computer on five key components and gives you a number for each, as well as an overall base score. This base score is only as good as your worst-performing component subscore. Base scores currently range from 1 to 7.9. If your PC is rated lower than 2 or 3, it might be time to consider a new PC, depending on what tasks you want to do with your computer.

    Change the size of virtual memory
    If you receive warnings that your virtual memory is low, you'll need to increase the minimum size of your paging file. Windows sets the initial minimum size of the paging file equal to the amount of random access memory (RAM) installed on your computer, and the maximum size equal to three times the amount of RAM installed on your computer. If you see warnings at these recommended levels, then increase the minimum and maximum sizes.

    Open System by clicking the Start Start button icon button , right-clicking Computer, and then clicking Properties.

    In the left pane, click Advanced system settings Administrator permission required. If you're prompted for an administrator password or confirmation, type the password or provide confirmation.

    On the Advanced tab, under Performance, click Settings.

    Click the Advanced tab, and then, under Virtual memory, click Change.

    Clear the Automatically manage paging file size for all drives check box.

    Under Drive[Volume Label], click the drive that contains the paging file you want to change.

    Click Custom size, type a new size in megabytes in the Initial size (MB) or Maximum size (MB) box, click Set, and then click OK.
    """

]


import time
import requests

# Author = Abhinav
# Date = 21 April 2021
# Purpose = For the python practise


def search_Engine(str, lis):
    result = list()
    lis.sort(key=len)
    for i in lis:
        if str.lower() in i.lower():
            result.append(i)
    return result


if __name__ == "__main__":
    search_str = input("Please Enter your query string : \n")

    if search_str == "":
        print("Plz Enter Something like string to find it\n")
        exit()
    else:
        startup_time = time.time()
        query = search_Engine(search_str, sentences)
        print(f"About {len(query)} results in just ({time.time() - startup_time}) sec.\n")
        for index, value in enumerate(query):
            print(f"{index+1}. \t{value}\n\n\n")

    # this part is optional as it is added just by Abhinav
    url = input("This is optional You can Enter a url and we can file checked that is Your string is present or not Or you can simply press Enter to skip this :\n")

    if url == "":
        print("All right Thank you!")
        exit()
    else:
        search_str = input("Enter the string you want to check whether it is present in the webpage or not : \n")
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print("Sorry! You are offline, We can't connect with the internet")
        else:
            if search_str.lower() in str(response.content).lower():
                print(f"Yes your string {search_str} is present in this webpage : {url}")
            else:
                print(f"Sorry! We didn't get {search_str} in {url} webpage")


