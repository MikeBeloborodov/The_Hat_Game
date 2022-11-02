interface Player {
  username: string;
}

export default interface SessionDetails {
  current_round: string;
  id: number;
  owner: {
    username: string;
  };
  team1: {
    name: string;
    points: number;
    players: Player[];
  };
  team2: {
    name: string;
    points: number;
    players: Player[];
  };
  words_per_player: number;
}
