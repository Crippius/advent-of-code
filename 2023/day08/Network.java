package day08;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Network {
    
    protected Map<String, Node> nodes; 
    private Node curr_pos;   

    public Network() {
        nodes = new HashMap<String, Node>();
        curr_pos = null;
    }

    public void addNode(Node node) {
        nodes.put(node.getName(), node);
        if (node.getName().equals("AAA"))
            curr_pos = node;
    }

    public Set<String> getNodes() {
        return nodes.keySet();
    }

    public void addNode(String curr, String left, String right) {

        if (!nodes.keySet().contains(left))
            nodes.put(left, new Node(left, null, null));
        if (!nodes.keySet().contains(right))
            nodes.put(right, new Node(right, null, null));
        if (!nodes.containsKey(curr))
            nodes.put(curr, new Node(curr, nodes.get(left), nodes.get(right)));
        else {
            nodes.get(curr).setLeft(nodes.get(left));
            nodes.get(curr).setRight(nodes.get(right));
        }
        if (nodes.get(curr).getName().equals("AAA")) {
            curr_pos = nodes.get(curr);
        }

    }

    public void followInstruction(int instr) {
        if (instr == 0)
            curr_pos = curr_pos.getLeft();
        if (instr == 1)
            curr_pos = curr_pos.getRight();

    }

    public String getCurr() {
        return curr_pos.getName();
    }

    public void setStartPosition(String start) {
        curr_pos = nodes.get(start);
    }

    @Override
    public String toString() {
        String print = "";
        for (Node n: nodes.values())
            if (n != null)
                print += n + "\n";
            else
                print += ":(\n";
        return print;

    }

}
