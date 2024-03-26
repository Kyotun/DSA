public class BadIndexFormatException extends Exception{
    private String message;

    public BadIndexFormatException(String msg){
        super(msg);
    }

    public void setMessage(String msg){
        this.message = msg;
    }
    public String getMessage(){
        return this.message;
    }
}
