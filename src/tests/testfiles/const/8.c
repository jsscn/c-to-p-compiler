
int f(int** i) {
    return 0;
}

int main() {
    int* const * a;
    int** b = a;
    f(a);
}