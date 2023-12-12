package day08;
public class Node {
    
    private String name;
    private Node left;
    private Node right;

    public Node(String name, Node left, Node right) {
        this.name = name;
        this.right = right;
        this.left = left;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    public void setRight(Node right) {
        this.right = right;
    }
    
    public Node getRight() {
        return right;
    }

    public Node getLeft() {
        return left;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        String print = "";
        print += name;
        print += ": ";
        if (left != null)
            print += left.getName();
        else
            print += ":(";
        print += " ";
        if (right != null)
            print += right.getName();
        else
            print += ":(";
        return print;
    }
}
