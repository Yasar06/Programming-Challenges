public class TinyLife {
    public static void main(String[] args) throws Exception {}

    public static boolean getCell(long world, int col, int row){
        if (col > 7) {
            return false;

        } else if (col < 0) {
            return false;

        }else {
            return true;
        }
    }
}
