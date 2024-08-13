class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.votes = {}

    def add_candidate(self, name):
        self.candidates[name] = 0
        self.votes[name] = []

    def cast_vote(self, name, vote):
        if name in self.candidates:
            self.candidates[name] += 1
            self.votes[name].append(vote)
            print("Vote cast successfully!")
        else:
            print("Candidate not found!")

    def view_votes(self):
        for name, count in self.candidates.items():
            print(f"{name}: {count} votes")
            print(f"Votes: {', '.join(self.votes[name])}")
            print("------------------------")


def main():
    voting_system = VotingSystem()

    while True:
        print("1. Add candidate")
        print("2. Cast vote")
        print("3. View votes")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter candidate name: ")
            voting_system.add_candidate(name)
        elif choice == "2":
            name = input("Enter candidate name: ")
            vote = input("Enter your vote (yes/no): ")
            voting_system.cast_vote(name, vote)
        elif choice == "3":
            voting_system.view_votes()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
