//
//  q2.h
//  mtd215
//
//  Created by Donaldson Tan on 27/7/25.
//
#include <string>
#include <iostream>

struct Player {
    std::string name;
    int rank;
};

int main(int argc, char* args[]) {
    
    // receive the name and rank of 10 players
    Player players[10];
    int totalRank = 0;
    for(int i = 0; i<10; i++) {
        std::cout << "Enter Player " << i + 1 << "'s name: ";
        std::cin >> players[i].name;
        std::cout << "Enter Player " << i + 1 << "'s rank: ";
        std::cin >> players[i].rank;
        std::cout << std::endl;
        totalRank += players[i].rank;
    }
    
    // create all possible partitions of players and search for the partition
    // leading to the min difference in rank between the 2 teams
    int minTeam1Rank = players[0].rank + players[1].rank + players[2].rank + players[3].rank + players[4].rank;
    int minDiff = abs(totalRank - 2 * minTeam1Rank);
    int team1[5] = {0,1,2,3,4};
    for(int i=0; i<6; i++) {
        for(int j=i+1; j<7; j++) {
            for(int k=j+1; k<8; k++) {
                for(int l=k+1; l<9; l++) {
                    for(int m=l+1; m<10; m++) {
                        // team1 consists of players i, j, k, l and m
                        int team1Rank = players[i].rank + players[j].rank + players[k].rank + players[l].rank + players[m].rank;
                        int diff = abs(totalRank - 2*team1Rank);
                        if (diff < minDiff) {
                            minDiff = diff;
                            team1[0] = i;
                            team1[1] = j;
                            team1[2] = k;
                            team1[3] = l;
                            team1[4] = m;
                            minTeam1Rank = team1Rank;
                        }
                    }
                }
            }
        }
    }
    
    std::cout << "Grouping..." << std::endl << std::endl;
    
    std::cout << "Group 1" << std::endl;
    for(int i=0; i<5; i++) {
        int j = team1[i];
        std::cout << players[j].name << " - performance rating: " << players[j].rank << std::endl;
    }
    std::cout << std::endl;
    
    std::cout << "Group 2" << std::endl;
    int j = 0;
    for(int i=0; i<6; i++) {
        int stop = i == 5 ? 10 : team1[i];
        while(j < stop) {
            std::cout << players[j].name << " - performance rating: " << players[j].rank << std::endl;
            j++;
        }
        j++;
    }
    std::cout << std::endl;
    
    std::cout << "The absolute rank difference between the teams is " << minDiff << std::endl;
    
    return 0;
}
