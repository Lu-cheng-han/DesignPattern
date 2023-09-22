 /**odd section*/
public static void odd (int n) {
    //new three stack A,B,C
    Stack<Integer> oA=new Stack<Integer>();
    Stack<Integer> oB=new Stack<Integer>();
    Stack<Integer> oC=new Stack<Integer>();
    int disk=0;                    //catch the pop
    int count=0;                //count the step
    for(int i=n+1;i>0;i--)
        oA.push(i);
    while(true)
    {    //A<->C section
        if(oC.empty()||oA.peek()<oC.peek())
        {
            disk=oA.pop();
            System.out.println("Step "+(count+1)+": move disk "+disk+" from A to C" );
            oC.push(disk);
            count++;
        }
        else if(oA.empty()||oA.peek()>oC.peek())
        {
            disk=oC.pop();
            System.out.println("Step "+(count+1)+": move disk "+disk+" from C to A");
            oA.push(disk);
            count++;
        }
        if(count==(int)Math.pow(2, n)-1)            //full step,break
            break;
        //A<->B section
        if(oB.empty()||oA.peek()<oB.peek())
        {
            disk=oA.pop();
            System.out.println("Step "+(count+1)+": move disk "+disk+" from A to B" );
            oB.push(disk);
            count++;
        }
        else if(oA.empty()||oA.peek()>oB.peek())
        {
            disk=oB.pop();
            System.out.println("Step "+(count+1)+": move disk "+disk+" from B to A");
            oA.push(disk);
            count++;
        }
        if(count==(int)Math.pow(2, n)-1)            //full step,break
            break;
        //B<->C section
        if(oB.empty()||oB.peek()>oC.peek())
        {
            disk=oC.pop();
            System.out.println("Step "+(count+1)+": move disk " +disk+" from C to B");
            oB.push(disk);
            count++;
        }
        else if(oC.empty()||oB.peek()<oC.peek())
        {
            disk=oB.pop();
            System.out.println("Step "+(count+1)+": move disk " +disk+" from B to C");
            oC.push(disk);
            count++;
        }
        if(count==(int)Math.pow(2, n)-1)            //full step,break
            break;
    }
}