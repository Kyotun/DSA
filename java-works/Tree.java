public class Tree {
    TreeNode root = null;

    public void insert(int value){
        TreeNode temp = this.root;
        TreeNode parent = this.root;

        if(root == null){
            this.root = new TreeNode(value);
        } else {

            while(temp != null){

                parent = temp;
                if (temp.value <= value){
                    temp = temp.left;
                } else {
                    temp = temp.right;
                }
                TreeNode mn = new TreeNode(value);
                if (parent.value >= value) {
                    parent.left = mn;
                } else {
                    parent.right = mn;
                }
            }
        }
    }

    public void printInorder() {
        if(root == null) return;
        privatePrintInorder(root);
        System.out.println();
    }

    public void privatePrintInorder(TreeNode mn) {
        if(mn == null) return;

        privatePrintInorder(mn.left);
        System.out.println(mn.value + " ");
        privatePrintInorder(mn.right);
    }
}