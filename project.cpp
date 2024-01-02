#include <iostream>
#include <conio.h>
#include <algorithm>
using namespace std;

struct Process 
{
    int id;
    int arrivalTime;
    int burstTime;
    int completionTime;
};

bool compareArrivalTime(const Process& p1, const Process& p2) 
{
    return p1.arrivalTime < p2.arrivalTime;
}

void FCFS()
{
    vector<Process> processes;

    int count = 1;
    char con;

    while (true) 
    {
        Process p;
        p.id = count;
        cout << "Process " << count << " Arrival Time: ";
        cin >> p.arrivalTime;
        cout << "Process " << count << " Burst Time  : ";
        cin >> p.burstTime;

        processes.push_back(p);

        cout << "Add more? (y/n): ";
        cin >> con;
        cout << "\n";

        if (con == 'n') {
            break;
        } else {
            count++;
            continue;
        }
    }

    sort(processes.begin(), processes.end(), compareArrivalTime);

    int currentTime = 0;
    int totalTurnaroundTime = 0;
    int total_Waiting_Time = 0;

    cout << "PID\tAT\tBT\tCT\tTT\tWT\n";
    
    for (Process& p : processes) {  // Remove 'const' to make it a non-const reference
        currentTime = max(currentTime, p.arrivalTime); // Wait if the process has not arrived yet
        p.completionTime = currentTime + p.burstTime;
        int turnaroundTime = p.completionTime - p.arrivalTime;
        int waiting_time = turnaroundTime - p.burstTime;
        totalTurnaroundTime += turnaroundTime;
        total_Waiting_Time += waiting_time;
            
        cout << p.id << "\t" << p.arrivalTime << "\t" << p.burstTime << "\t" << p.completionTime << "\t" << turnaroundTime << "\t" << waiting_time << "\n";

        currentTime = p.completionTime;
    }

    cout << "Average Turnaround Time: " << static_cast<double>(totalTurnaroundTime) / processes.size() << "\n";
    cout << "Average Turnaround Time: " << static_cast<double>(total_Waiting_Time) / processes.size() << "\n";
}

void preimptive()
{
    int choice;

    cout << "[1] - FIFS\n";
    cout << "[2] - ";
    cout << "[3] - ";
    cin  >> choice;
    system("Cls");

    switch(choice)
    {
        case 1:
        {
            FCFS();
        }
    }
}

int main()
{   
    system("Cls");
    int choice;
    
    cout << "Choose a scheduler\n";
    cout << "------------------\n";
    cout << "[1] - Preimptive\n";
    cout << "[2] - Non-Preimptive\n";
    cout << ": "; 
    cin  >> choice;
    system("Cls");

    switch(choice)
    {
        case 1:
        {
            preimptive();
            break;
        }
        system("Cls");
    }
    return 5;
}