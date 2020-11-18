#프린터

#include <string>
#include <vector>
#include <deque>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 1;

    deque<pair<int, int>> dq;
    for(int i = 0; i<priorities.size(); i++){
        dq.push_back(pair<int,int>(priorities[i],i));
    }    
    

    while(1){
        for(int j = 0; j<dq.size(); j++){
            if(dq.front().first < dq[j].first){
                dq.push_back(dq.front());
                dq.pop_front();
                j = 0;
                continue;
            }
            if(j == dq.size() -1)
                break;
        }
        if(dq.front().second == location){
            break;
        }
        else{
            dq.pop_front();
            answer++;
        }
    }

    return answer;
}