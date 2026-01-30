#include <bits/stdc++.h>
using namespace std;

typedef vector<double> VD;
typedef vector<VD> VVD;

/* Matrix multiplication */
VVD multiply(const VVD &A, const VVD &B) {
    int r = A.size(), c = B[0].size(), k = B.size();
    VVD res(r, VD(c, 0.0));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            for (int t = 0; t < k; t++)
                res[i][j] += A[i][t] * B[t][j];
    return res;
}

/* Matrix transpose */
VVD transpose(const VVD &A) {
    int r = A.size(), c = A[0].size();
    VVD T(c, VD(r));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            T[j][i] = A[i][j];
    return T;
}

/* Matrix inverse (Gauss-Jordan) */
VVD inverse(VVD A) {
    int n = A.size();
    VVD I(n, VD(n, 0));
    for (int i = 0; i < n; i++) I[i][i] = 1;

    for (int i = 0; i < n; i++) {
        double diag = A[i][i];
        for (int j = 0; j < n; j++) {
            A[i][j] /= diag;
            I[i][j] /= diag;
        }
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = A[k][i];
                for (int j = 0; j < n; j++) {
                    A[k][j] -= factor * A[i][j];
                    I[k][j] -= factor * I[i][j];
                }
            }
        }
    }
    return I;
}

int main() {
    int m, n;
    cin >> m >> n;

    // X matrix with bias term
    VVD X(n, VD(m + 1, 1.0));
    VVD y(n, VD(1));

    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= m; j++)
            cin >> X[i][j];
        cin >> y[i][0];
    }

    VVD XT = transpose(X);
    VVD theta = multiply(
                    multiply(inverse(multiply(XT, X)), XT),
                    y
                );

    int q;
    cin >> q;
    cout << fixed << setprecision(2);

    while (q--) {
        VD features(m + 1, 1.0);
        for (int i = 1; i <= m; i++)
            cin >> features[i];

        double result = 0;
        for (int i = 0; i <= m; i++)
            result += theta[i][0] * features[i];

        cout << result << endl;
    }

    return 0;
}
