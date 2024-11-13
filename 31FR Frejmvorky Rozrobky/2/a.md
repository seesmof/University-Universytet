Listing
  type: private OR flat OR new 
  owner: User
User 
  type: user OR manager 
  listings: list[Listing]
  chosen: list[Listing]
Meeting 
  status: pending OR visited OR canceled
  score: 1 OR 2 OR 3
  listing: Listing

confirmMeeting: Meeting.status=visited
viewAllMeetings: return list[Meeting] Meeting.listing.owner==current_user__owner
viewChosenMeetings return [Listing for Listing in viewAllMeetings() if Listing in current_user__owner.chosen]
cancelMeeting: Meeting.status=canceled