namespace seven {
    public class Estate {
        public int ID { get; set; }
        public User Owner { get; set; }
        public string Title { get; set; }
        public string Kind { get; set; }
        public int Price { get; set; } = 0;
    }
}
