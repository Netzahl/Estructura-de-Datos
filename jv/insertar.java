public class insertar {
    
    public static void main(String[] args) {
        
        int[] num = {1,2,3,4,5}, newnum = new int[5];
        int newElement = 76, posicion = 2, j= 0;

        for (int idx = 0; idx < num.length; idx++) {
            if ( posicion == idx + 1 ) {
                newnum[idx] = newElement;
                j++;
            }
            else{
                newnum[idx] = num[idx-j];
            }
            
        }

        for(int n:newnum){
            System.out.print(n + ", ");
        }

    }
}
