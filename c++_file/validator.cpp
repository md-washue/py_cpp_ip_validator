#include <iostream>
#include <string>

#ifdef _WIN32
	#include <winsock2.h>
	#include <ws2tcpip.h>
	#pragma comment(lib,"Ws2_32.lib")
#else
	#include <arpa/inet.h>
#endif

int main(int argc, char* argv[]){
	if (argc !=2){


		std::cout << "Invalid Address" << std::endl;
		return 1;
	}
	std::string ip = argv[1];
	unsigned char buf[sizeof(struct in6_addr)];

	if(inet_pton(AF_INET,ip.c_str(),buf)==1){
		std::cout<<"Valid IPv4" << std::endl;
		return 0;
	}

	if(inet_pton(AF_INET6, ip.c_str(),buf)==1){
		std::cout<<"Valid IPv6" <<std::endl;
		return 0;

	}
	std::cout<<"Invalid Address" << std::endl;
	return 1;
}
