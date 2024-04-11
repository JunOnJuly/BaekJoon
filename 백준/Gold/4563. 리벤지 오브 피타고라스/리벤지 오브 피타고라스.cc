#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <cmath>

using namespace std;

int main(void) {
	while (true) {
		// 입력
		long long int A;
		cin >> A;
		// 입력이 0 이면 끝
		if (A == 0) return 0;
		// 카운트
		int cnt = 0;
		// A^2 + B^2 = C^2 -> A^2 = (C - B)(C + B)
		// A^2
		long long int pow_A = pow(A, 2);
		// 순회하며 약수 쌍 구하기
		for (long long int i = 1; i <= A - 1; i++) {
			// i 가 약수면
			if (pow_A % i == 0) {
				// (C-B) = i, (C+B) = pow_A/i ( (C-B) < (C+B) , i < pow_A/i )
				// 2B = pow_A/i - i
				// (pow_A/i - i) 가 2의 배수여야 자연수 가능
				// B가 2의 배수고 A 보다 크면
				if ((pow_A / i - i) % 2 == 0 and (pow_A / i - i) / 2 > A) {
					cnt += 1;
				}
			}
		}
		cout << cnt << "\n";
	}
}