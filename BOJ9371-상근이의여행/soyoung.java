import java.util.*;
class Main {

  static int N,M,result;
  static int arr[][];
  static boolean visit[];
  //static Tree[] nodes;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt(); //테스트케이스 수

    for(int i=0; i<T; i++){
      //String in = sc.next();
      N = Integer.parseInt(sc.next());
      M = Integer.parseInt(sc.next());

      int a,b;
      arr = new int[N+1][N+1];
      visit = new boolean[N+1];
      result = 0;

      for ( int j=0; j<M; j++){
        a = Integer.parseInt(sc.next());
        b = Integer.parseInt(sc.next());

        arr[a][b] = 1;
        arr[b][a] = 1;
      }

      for ( int j=1; j<=N; j++){
        for (int k=1; k<=N; k++){
          System.out.print(arr[j][k]);
        }
        System.out.println();
      }
      bfs();

      System.out.println(result-1);
    }
  }
  private static void bfs() {
    // TODO Auto-generated method stub
    Queue<Integer> queue = new LinkedList<Integer>();
    queue.add(1);
    visit[1] = true;
    while(!queue.isEmpty()) {
        result++;
        System.out.println("result: "+result);
        int val = queue.poll();
        System.out.println("poll val: "+ val);
        for(int i=1; i<=N; i++) {
            //System.out.println(arr[val][i] + ", " +visit[i] );
            // 연결된 애 중애 방문했는지 체크 
            if(arr[val][i]!=0 && !visit[i]) {
                visit[i] = true;
                queue.add(i);
                System.out.println("방문안함 add val: "+ i);
            }
        }
    }
  }
}
