(module
  ;; Define a function to be called from our host
  (func $run_loop
    (param $range i64)
    (result i64)

    (local $i i64)

    (loop $my_loop
      ;; add one to $i
      local.get $i
      i64.const 1
      i64.add
      local.set $i

      ;; if $i is less than 10 branch to loop
      local.get $i
      local.get $range
      i64.lt_s
      br_if $my_loop
    )

    local.get $i
  )

  ;; Export the wasmprint function for the host to call.
  (export "run_loop" (func $run_loop))
)