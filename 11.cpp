#include <cstdio>
#include <utility>

const int X = 91;
const int Y = 97;
char input[Y][X];
char room[2][Y][X];

const char OCCUPIED = '#';
const char EMPTY = 'L';
const char FLOOR = '.'; 

void get_input() {
    for(int i = 0; i < Y; i++) {
        scanf("%s", input[i]);
    }
}

const std::pair<int, int> directions[] = {
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, -1},
    {0, 1},
    {1, -1},
    {1, 0},
    {1, 1}
};

bool in_bounds(int y, int x) {
    return x >= 0 && x < X && y >= 0 && y < Y;
}

int get_occupied_adjacent_simple(int y, int x, int current, bool stop_on_first) {
    int occupied_adjacent = 0;
    for(int i = 0; i < 8; i++) {
        int dy = directions[i].first;
        int dx = directions[i].second;
        int new_y = y + dy;
        int new_x = x + dx;
        if (in_bounds(new_y, new_x) && room[current][new_y][new_x] == OCCUPIED) {
            ++occupied_adjacent;
            if (stop_on_first) {
                return 1;
            }
        }
    }   
    return occupied_adjacent;
}

int get_occupied_adjacent_linear(int y, int x, int current, bool stop_on_first) {
    int occupied_adjacent = 0;
    for(int i = 0; i < 8; i++) {
        int dy = directions[i].first;
        int dx = directions[i].second;
        int new_y = y + dy;
        int new_x = x + dx;
        while (in_bounds(new_y, new_x) && room[current][new_y][new_x] == FLOOR) {
            new_y += dy;
            new_x += dx;
        }
        if (in_bounds(new_y, new_x) && room[current][new_y][new_x] == OCCUPIED) {
            ++occupied_adjacent;
            if (stop_on_first) {
                return 1;
            }
        }
    }
    return occupied_adjacent;
}

int do_simulation(bool part2 = false) {
    for (int y = 0; y < Y; y++) {
        for (int x = 0; x < X; x++) {
            room[0][y][x] = input[y][x];
        }
    }
    int threshold = part2 ? 5 : 4;
    int iter = 0;
    bool active = true;
    while (active) {
        int current = iter % 2;
        int next = 1 - iter % 2;
        active = false;
        for(int y = 0; y < Y; y++) {
            for(int x = 0; x < X; x++) {
                if (room[current][y][x] == FLOOR) {
                    room[next][y][x] = FLOOR;
                    continue;
                }
                bool stop_on_first = room[current][y][x] == EMPTY;
                int occupied_adjacent = part2
                    ? get_occupied_adjacent_linear(y, x, current, stop_on_first)
                    : get_occupied_adjacent_simple(y, x, current, stop_on_first);
                if (room[current][y][x] == EMPTY && occupied_adjacent == 0) {
                    room[next][y][x] = OCCUPIED;
                    active = true;
                } else if (room[current][y][x] == OCCUPIED && occupied_adjacent >= threshold) {
                    room[next][y][x] = EMPTY;
                    active = true;
                } else {
                    room[next][y][x] = room[current][y][x];
                }
            }
        }
        iter++;
    }
    int ans = 0;
    for (int y = 0; y < Y; y++) {
        for(int x = 0; x < X; x++) {
            ans += room[0][y][x] == OCCUPIED;
        }
    }
    return ans;    
}

int part1() {
    return do_simulation();
}

int part2() {
    return do_simulation(true);
}


int main() {
    get_input();
    printf("%d\n", part1());
    printf("%d\n", part2());
}