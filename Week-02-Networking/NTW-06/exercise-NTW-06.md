#  Subnetting

Subnetting is the process of logically creating small groups networks from a given large network. It increases the security and enables the efficiency of networking as it is relatively easy to manage small networks rather than managing one big network.

## Key terminologies

CIDR -Classless Inter Domain Range- it indicates the number of network bits eg-/24 means 24 bits are reserved for networking.

Subnet mask - Helps to identify which the portion belonging to the host and also to the subnet.

## Exercise

Create a network architecture that meets the following requirements:

- 1 private subnet accessible only from within the LAN. This subnet must be able to accommodate at least 15 hosts.
- 1 private subnet that has internet access via a NAT gateway. This subnet must be able to accommodate a minimum of 30 hosts (the 30 hosts does not include the NAT gateway).
- 1 public subnet with an internet gateway. This subnet must be able to accommodate at least 5 hosts (the 5 hosts does not include the internet gateway).
- Place the architecture you created including a short explanation in the Github repository you shared with the learning coach.
### Sources

https://ipcisco.com/lesson/ip-subnetting-and-subnetting-examples/

https://www.techtarget.com/searchnetworking/definition/CIDR

https://www.ipxo.com/blog/what-is-subnet-mask/

http://www.aboutmyip.com/AboutMyXApp/SubnetCalculator.jsp

### Overcome challenges

Had to look up how to do the calculations for subnetting.
Started with 192.168.0.0/24 as the base ip address.

The largest number of host requirement in the given case is 30(excluding NAT).Using the eqn (2**n - 2) i.e. considering the fact that the first ip and last ip are not usable ip addresses, the group size of 64 was chosen(2 to the power of 6).So the number of host bites is 6, which means the number of network bits is 26(subtracting from 32).Thus  the base address was divided into 4 equal blocks of 192.168.0.0/26 to obtain 192.168.0.0/26, 192.168.0.64/26, 192.168.0.128/26, 192.168.0.192/26.
The first set of this block was reserved to accomodate 30 hosts(Group size is 64 which means 62 usable addresses are available)

The second set of 192.168.0.64/26 was taken and applying the above logic in a similar fashion was divided into 2 subnets namely 192.168.0.64/27 and 192.168.0.96/27, each of group size 32. This subnet was used to accomodate 15 hosts.

The third block of 192.168.0.128/26 was taken and divided into groups of size 8.this block of 192.168.0.128/29 was used for accomodating 5 hosts + 1 IGW. Since the group size is 8, the number of usable ip addresses is 6 which gets fully utilized in this case. In case some reservations are required for future growth, instead of 
192.168.0.128/29, 192.168.0.128/28 can be made use of. This can accomodate 14 hosts(group size-16) which more than the required number of 6 usable ip addresses.

### Results
Subnet A can be used to host 31 ip addresses, subnet B can be used to accomodate 16 ip addresses and subnet C can host 5 ip addresses.

##### ![NTW-06-01img](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-02/NTW/NTW-06-subnet.png)











