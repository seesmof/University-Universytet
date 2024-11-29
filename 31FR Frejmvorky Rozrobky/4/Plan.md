# Task
## Raw
- buy Estate
- sell Estate
- Estate kind Home or Flat or New
- sell Estate of kind New only by Admin 
- set Meeting for Estate 
- Meeting status Wait or Done or Skip
- Meeting score Bad or Okay or Fine
- Owner see Meetings for all Estate or for Chosen
- Owner change Meeting status 
- Owner remove Estate 
- Owner change Estate 

## Processed
- Estate 
  - def buy 
  - def sell 
    - of kind New only by Admin 
  - self.kind Home or Flat or New
- Meeting
  - self.Estate 
  - self.status Wait or Done or Skip
  - self.score Bad or Okay or Fine
- User 
  - def seeMeetings
    - for all Estate
    - for chosen Estate
  - def changeMeeting
  - def removeMeeting

# Architecture
## Database
user 
  int id 
  string name 
  bool admin = 0
estate 
  int id 
  int owner_id
  string title
  string kind (Home or Flat or New)
meeting 
  int id 
  int sender_id
  int target_id
  string status (Wait or Done or Skip) = Wait
  string score (Bad or Okay or Fine)

## Classes
User 
  int ID 
  string Name 
  bool Admin
Estate 
  int ID 
  User Owner
  string Title
  string Kind (Home or Flat or New)
Meeting 
  int ID 
  User Sender
  Estate Target
  string Status (Wait or Done or Skip) = Wait
  string Score (Bad or Okay or Fine)
Session
  bool Entered
  User Client
  list<Estate> Owned
  list<Meeting> Plan

## Features 
- Request User status change 
- User buy Estate
- Owner sell Estate
  - of kind New only by Admin 
- User set Meeting for Estate 
- Owner see Meeting's for selected Estate
- Owner see Meetings for all Estate
- Owner change Meeting status 
- Owner remove Estate 
- Owner change Estate 

```
1 Edit profile
2 Buy estate
3 Sell estate
4 Edit estate
5 Remove estate
6 Schedule meeting
7 Rate meeting (Viewer)
8 Process meeting (Owner)
```

