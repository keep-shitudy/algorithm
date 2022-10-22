public class Solution_Lv2_예상대진표 {
    // 게임진행 후 1-N/2까지 다시 번호배정
    // 1,2 -> 1번 //3,4 -> 2번
    // answer : A와B가 만나는 라운드 수

    public static void main(String[] args) {
        int n = 8;
        int a = 4;
        int b = 7;

        int ans = solution(n, a, b);
        System.out.println(ans);
    }

    public static int solution(int n, int a, int b) {
        int answer = 0;

        a = a - 1;
        b = b - 1;
        // 1,2 를 2로 나누면 몫은 0,1
        // 0,1 을 2로 나누면 몫은 0,0
        // 2,3 를 2로 나누면 몫은 1,1

        for (int i = 0; i < Math.sqrt(n); i++) {
            answer++;
            if (a / 2 == b / 2) {
                break;
            } else {
                a /= 2;
                b /= 2;
            }
        }

        return answer;
    }
}
