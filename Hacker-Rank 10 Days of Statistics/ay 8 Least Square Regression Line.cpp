#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int x[5] = {95, 85, 80, 70, 60};
    int y[5] = {85, 95, 70, 65, 70};

    int n = 5;
    double sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;

    for (int i = 0; i < n; i++) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] * x[i];
    }

    double b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    double a = (sumY / n) - b * (sumX / n);

    double xValue = 80;
    double yValue = a + b * xValue;

    cout << fixed << setprecision(2) << yValue << endl;
    return 0;
}
