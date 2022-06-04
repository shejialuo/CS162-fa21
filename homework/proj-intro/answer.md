# Project 0 Answer

1. The virtual address the program tried to access is `0xc0000008`.
2. eip=`0x80488ee`.
3. _start. Use `objdump -D proj-intro/src/userprog/build/tests/userprog/do-nothing | grep '80488ee'`.
4. `void _start(int argc, char* argv[]) { exit(main(argc, argv)); }`. For the assembly
code, it is the call convention.
5. The reason is super easy. `mov 0xc(%ebp), %eax`.
6. Using `info threads` to find the thread name is `main`. And use `info address main` to
find the address is `0xc0020306`.
   + Thread 1: `pintos-debug: dumplist #0: 0xc000e000 {tid = 1, status = THREAD_RUNNING, name = "main", '\000' <repeats 11 times>, stack = 0xc000edbc "\001", priority = 31, allelem = {prev = 0xc0039c18 <all_list>, next = 0xc0104020}, elem = {prev = 0 xc0039c08 <ready_list>, next = 0xc0039c10 <ready_list+8>}, pcb = 0xc010500c, magic = 3446325067}`
   + Thread 2: `pintos-debug: dumplist #1: 0xc0104000 {tid = 2, status = THREAD_BLOCKE,name = "idle", '\000' <repeats 11 times>, stack = 0xc0104f14 "", priority = 0, allelem = {prev = 0xc000e020, next = 0xc0039c20 <all_list+8>}, elem = {prev = 0xc0039c08 <ready_list>, next = 0xc0039c10 <ready_list+8>}, pcb = 0x0, magic = 3446325067}`
7. The backtrace is:
   + #0  process_execute (file_name=0xc0007d50 "do-nothing") at ../../userprog/process.c:58
          `process_execute(const char* file_name);`
   + #1  0xc0020888 in run_task (argv=0xc0039b0c <argv+12>) at ../../threads/init.c:279
          `static void run_task(char** argv);`
   + #2  0xc00209fe in run_actions (argv=0xc0039b0c <argv+12>) at ../../threads/init.c:352
          `run_actions(argv);`
   + #3  0xc00203d9 in main () at ../../threads/init.c:138
          `int main(void);`
8. The `start_process` create the new PCB, and starts a new thread `do-nothing`.
Use `dumplist &all_list thread allelem` again.
9. `struct thread* t = thread_current();`
10. `$1 = {edi = 0x0, esi = 0x0, ebp = 0x0, esp_dummy = 0x0, ebx = 0x0, edx = 0x0,ecx = 0x0, eax = 0x0, gs = 0x23, fs = 0x23, es = 0x23, ds = 0x23, vec_no = 0x0, error_code = 0x0, frame_pointer = 0x0, eip = 0x80488e8, cs = 0x1b, eflags =0x202, esp = 0xc0000000, ss = 0x23}`
11. Because the interruption is kernel-level code, so the processor should switch modes.
12. The registers' information is
    ```
      eax            0x0      0
      ecx            0x0      0
      edx            0x0      0
      ebx            0x0      0
      esp            0xc0000000       0xc0000000
      ebp            0x0      0x0
      esi            0x0      0
      edi            0x0      0
      eip            0x80488e8        0x80488e8
      eflags         0x202    [ IF ]
      cs             0x1b     27
      ss             0x23     35
      ds             0x23     35
      es             0x23     35
      fs             0x23     35
      gs             0x23     35
    ```
13. The output is:
    + #0  _start (argc=-268370093, argv=0xf000ff53) at ../../lib/user/entry.c:6
    + #1  0xf000ff53 in ?? ()