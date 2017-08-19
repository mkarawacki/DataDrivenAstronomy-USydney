UPDATE Planet SET kepler_name=NULL WHERE status <> 'CONFIRMED'; DELETE FROM Planet where radius < 0;
select * from planet;