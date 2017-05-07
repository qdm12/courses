# Programming language course, Spring 2017

## Java and Scala programming assignment

### What is it?
Highlights OOP possibilities in Java and Scala

### Setup and run
1. Initial setup
    - Use Vagrant
        1. Make sure you have [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html).
        2. Download this assignment, `cd` to its directory with a terminal.
        3. Enter `vagrant up` and then `vagrant ssh` to log in the VM.
        4. In the VM, enter `cd /vagrant` to go to the shared directory.
    - If you have a Linux OS
        1. Install **java dev kit** and **scala** with `sudo apt-get -y install openjdk-7-jdk scala`
        2. Download this assignment, `cd` to its directory with a terminal.
2. Enter `javac Part1.java` to compile the Java Part.
3. Enter `java Part1` to run the program.
4. It should output the following content:
   ```shell
   m1 = [ A<1>  A<2>  A<3>  A<4>  A<5> ]
   m2 = [ B<1>  B<2>  B<3>  B<4>  B<5>  A<6> ]
   m1 is less than m2
   m1 + m2 = [ A<1>  A<2>  A<3>  A<4>  A<5>  B<1>  B<2>  B<3>  B<4>  B<5>  A<6> ]
   ```
5. Enter `scalac Part2.scala` to compile the Scala part.
6. Enter `scala Part2` to run the program.
7. It should output the following content:
   ```shell
   A<3>
   B<4,5>
   A<10>
   B<11,12>
   ((A<2>,A<3>,),A<4>,B<4,1>)
   A<3>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
   A<5>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
   B<2,1>is found in ((A<2>,A<3>,),A<4>,B<4,1>)
   B<4,2>is not found in ((A<2>,A<3>,),A<4>,B<4,1>)
   ```

### Assignment description
All the assignment is described in the comments in both parts.