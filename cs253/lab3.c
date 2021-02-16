#include<iostream>
#include<vector>
#include<string>
#include<set> 
#include<fstream>
using namespace std;


int main(){
	vector<int> v = {8,9999,78888,2313,12312,213,33,2,210,0,1,2,1,3};
	string s;
	multiset<char> mul;
	set<char> se;
	ifstream ifs("/etc/resolv.conf",ifstream::in);
	char c  =ifs.get();
	
	for(size_t i=0;i<v.size();i++){
		if(v[i]==0)
			break;
		cout<<v[i]<<'\n';	}
		

	while(ifs.good()){
		s.insert(c);
		c=ifs.get();}
		
	ifs.close;
	
	
	for (size_t i=0;i<s.size();i++){
		mul.insert(s[i]);
	}
	
	for(size_t i=0;i<mul.size();i++){
		se.insert(mul[i]);
	}
	
	
	cout<<s<< s.size()<<'\n';
	cout<<mul<<mul.size()<<'\n';
	cout<<se<<se.size()<<'\n';
	
	
	return 0;


}