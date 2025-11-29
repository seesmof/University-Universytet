namespace seven {
    public class UtilityFunctions {
        public bool checkEstateKind(string kind){
            return kind != EstateKind.Home && kind != EstateKind.Flat && kind != EstateKind.New ? false : true;
        }
        public bool checkMeetingStatus(string status){
            return status != MeetingStatus.Wait && status != MeetingStatus.Done && status != MeetingStatus.Skip ? false : true;
        }
        public bool checkMeetingScore(string score){
            return score != MeetingScore.Bad && score != MeetingScore.Okay && score != MeetingScore.Fine ? false : true;
        }
    }
}
