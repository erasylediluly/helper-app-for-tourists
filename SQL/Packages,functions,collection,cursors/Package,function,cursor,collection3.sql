CREATE OR REPLACE PROCEDURE file_to_blob (p_blob      IN OUT NOCOPY BLOB,
                                          p_dir       IN  VARCHAR2,
                                          p_filename  IN  VARCHAR2)
AS
  l_bfile  BFILE;

  l_dest_offset INTEGER := 1;
  l_src_offset  INTEGER := 1;
BEGIN
  l_bfile := BFILENAME(p_dir, p_filename);
  DBMS_LOB.fileopen(l_bfile, DBMS_LOB.file_readonly);
  DBMS_LOB.trim(p_blob, 0);
  IF DBMS_LOB.getlength(l_bfile) > 0 THEN
    DBMS_LOB.loadblobfromfile (
      dest_lob    => p_blob,
      src_bfile   => l_bfile,
      amount      => DBMS_LOB.lobmaxsize,
      dest_offset => l_dest_offset,
      src_offset  => l_src_offset);
  END IF;
  DBMS_LOB.fileclose(l_bfile);
END file_to_blob;

DECLARE
  l_blob   BLOB;
BEGIN
  SELECT image
  INTO   l_blob
  FROM   place
  WHERE  id = 1
  FOR UPDATE;

  file_to_blob (p_blob     => l_blob,
                p_dir      => 'C:\Users\Erasy\Desktop\Database2\QT\Images\1.jpg',
                p_filename => '1.jpg');
END;